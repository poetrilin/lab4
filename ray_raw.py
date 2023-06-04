import ray
import math
import time
import random

ray.shutdown()
ray.init()

# 定义 Progress Actor


@ray.remote
class ProgressActor:
    def __init__(self, total_num_samples: int):
        self.total_num_samples = total_num_samples
        self.num_samples_completed_per_task = {}

    def report_progress(self, task_id: int) -> None:
        self.num_samples_completed_per_task[task_id] = 1

    def get_progress(self) -> float:
        return (
            sum(self.num_samples_completed_per_task.values()) /
            self.total_num_samples
        )

# 定义 Worker Actor


@ray.remote
def sampling_task(task_id: int,
                  progress_actor: ray.actor.ActorHandle) -> int:
    num_inside = 0
    
    x, y = random.uniform(-1, 1), random.uniform(-1, 1)
    if math.hypot(x, y) <= 1:
        num_inside += 1

        # # Report progress every 1 million samples.
        # if (i + 1) % 1_000_000 == 0:
        #     # This is async.
        #     progress_actor.report_progress.remote(task_id, i + 1)

    # Report the final progress.
    progress_actor.report_progress.remote(task_id)
    return num_inside


# 初始部署参数
# 创建进度 Actor
# Change this to match your cluster scale.
# TOTAL_NUM_SAMPLES = 8
# NUM_SAMPLES_PER_TASK = 1_000
# TOTAL_NUM_SAMPLES = TOTAL_NUM_SAMPLES * NUM_SAMPLES_PER_TASK
TOTAL_NUM_SAMPLES = 100_0000
# Create the progress actor.
progress_actor = ProgressActor.remote(TOTAL_NUM_SAMPLES)

# 创建并执行所有采样任务的时间戳
start_time = time.time()

# Create and execute all sampling tasks in parallel.
results = [
    sampling_task.remote(i, progress_actor)
    for i in range(TOTAL_NUM_SAMPLES)
]

# 调用 Progress Actor
# Query progress periodically.
# while True:
#     progress = ray.get(progress_actor.get_progress.remote())
#     print(f"Progress: {int(progress * 100)}%")

#     if progress == 1:
#         break

#     time.sleep(1)


# 最后,从远程采样任务中获取圆内的样本数并计算 π。

# Get all the sampling tasks results.
total_num_inside = sum(ray.get(results))
estimate_pi = (total_num_inside * 4) / TOTAL_NUM_SAMPLES
print(f"Estimated value of π is: {estimate_pi}")

# Print the total execution time.
ray.get(results)

# 计算平均任务执行时间
execution_time = time.time() - start_time
average_execution_time = execution_time / TOTAL_NUM_SAMPLES

# 计算吞吐量
throughput = TOTAL_NUM_SAMPLES / execution_time

print(f"Total execution time: {execution_time} seconds")
print(f"Average task execution time: {average_execution_time} seconds")
print(f"Throughput: {throughput} samplescond")

# 计算估计值的相对误差
true_pi = math.pi
relative_error = abs((true_pi - estimate_pi) / true_pi)
print(f"Relative Error: {relative_error}")