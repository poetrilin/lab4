# RAY的部署及测试
参考: [RAY主页](https://docs.ray.io/en/latest/index.html)
 
 注: 本文已发布到[Blog](http://www.poetrilin.com/2023/06/03/Ray%E9%83%A8%E7%BD%B2%E4%B8%8E%E6%B5%8B%E8%AF%95/)


## 选定一个与选题对计算类任务

###  π 的蒙特卡洛估计

原理:该方法通过在 2x2 正方形内随机采样点来工作。我们可以使用以原点为中心的单位圆内包含的点的比例来估计圆的面积与正方形的面积之比。鉴于我们知道真实的比率是 π/4，我们可以将我们的估计比率乘以 4 来近似 π 的值。我们为计算此近似值而采样的点越多，该值就越接近 π 的真实值。



## 完成单机版部署并进行性能测试 

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

于是可以直接运行我们的代码

#### 测试

我们测试的是吞吐量和平均任务执行时间

程序代码见[test代码](./ray_test.ipynb).



## 参数优化

详见[性能测试文档](./性能测试.md)

## 分布式与docker部署

见[部署说明](./部署说明.md)