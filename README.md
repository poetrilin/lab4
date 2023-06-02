# RAY的部署及测试
参考:
1. [RAY主页](https://docs.ray.io/en/latest/index.html)
2. [本文的在线lab]
3. Blog


## 选定一个与选题对计算类任务

###  π 的蒙特卡洛估计
原理:该方法通过在 2x2 正方形内随机采样点来工作。我们可以使用以原点为中心的单位圆内包含的点的比例来估计圆的面积与正方形的面积之比。鉴于我们知道真实的比率是 π/4，我们可以将我们的估计比率乘以 4 来近似 π 的值。我们为计算此近似值而采样的点越多，该值就越接近 π 的真实值。

### 性能指标:

- 平均任务执行时间（Average Task Execution Time）：计算完成所有任务所需的平均时间。这个指标可以反映系统的整体性能。

- 吞吐量（Throughput）：表示单位时间内完成的任务数量。高吞吐量表示系统具有较高的并发处理能力。
  
- IOPS: 这个指标衡量单位时间内完成的输入/输出操作次数。对于涉及磁盘读写等操作的任务，高IOPS表示系统能够快速进行数据读写操作。
  
- 内存占用：可以使用Python的内存分析工具，如memory_profiler模块，来监测程序的内存使用情况。通过监测程序的内存使用情况，可以评估系统的内存占用情况。对于内存密集型任务，了解系统的内存占用情况可以帮助确定系统的性能和资源利用情况。

- 网络带宽：可以使用Ray的Dashboard来监测集群的网络带宽使用情况，从而评估网络带宽的性能。评估网络带宽的性能可以帮助确定系统在分布式计算和通信过程中的效率和稳定性。

这些指标综合考虑了任务执行时间、并发处理能力、数据读写效率、资源利用情况以及网络通信性能，能够全面评估RAY框架的性能和效果。

## 完成单机版部署并进行性能测试 
### 环境配置
创建一个新的虚拟环境(不在此赘述)安装ray的最小依赖`pip install ray`,如果成功你将看到如下类似结果：
```shell
Successfully installed aiosignal-1.3.1 attrs-23.1.0 certifi-2023.5.7 charset-normalizer-3.1.0 click-8.1.3 colorama-0.4.6 distlib-0.3.6 filelock-3.12.0 frozenlist-1.3.3 grpcio-1.51.3 idna-3.4 jsonschema-4.17.3 msgpack-1.0.5 numpy-1.24.3 platformdirs-3.5.1 protobuf-4.23.2 pyrsistent-0.19.3 pyyaml-6.0 ray-2.4.0 requests-2.31.0 urllib3-2.0.2 virtualenv-20.21.0
```

此时运行
```python
import ray

ray.init()
```
会提示你ray已经启动并且Dashboard:	http://127.0.0.1:8265

于是可以直接运行我们的代码(具体代码见[仓库]())

