大语言模型在长上下文场景下的 latency 表现，会随 context window 扩展而变化。模型在进行推理时，throughput 与首 token 延迟分别影响离线任务和交互式任务。

现有方案会压缩 KV cache，或者对 attention 进行稀疏化。不同做法会改变速度、显存占用和输出质量，不能只用单一指标判断。
