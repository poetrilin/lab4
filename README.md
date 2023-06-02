# RAY的部署及测试
参考:
1. [RAY主页](https://docs.ray.io/en/latest/index.html)
2. [本文的在线lab]
3. Blog

## 单机
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

性能指标:

- 总运行时间(加速比)：加速比 = 原来程序执行时间 / 部署RAY程序执行时间。

- 单任务的延时
  
- IOPS是指任务在单位时间内可以完成的输入/输出操作次数
  
- 内存占用：可以使用Python的内存分析工具，如memory_profiler模块，来监测程序的内存使用情况。

- 网络带宽：可以使用Ray的Dashboard来监测集群的网络带宽使用情况，从而评估网络带宽的性能。