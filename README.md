# 🦜️🔗 ChatLangChain

最近想做一个基于本地文档的QA问答，参考了LangChain官方出品的一个仓库chat-langchain，它使用的本地文档是LangChain官网，而我的需求本地文档是一个GitHub仓库，为此改写和修改了一些代码，放到了https://github.com/ywdblog/chat-langchain。

在这个过程中，遇到最大的问题是LangChain包版本的问题，它的更新太频繁了，而且函数不是向前兼容的，所以难免会遇到一些问题。

1：GitLoader

如果想使用Github仓库，则可以使用GitLoader：

```
$  ./ingest_git.sh
```

另外建议设置以下环境变量：

```
export OPENAI_API_KEY=""
export OPENAI_API_BASE=""
```

这个非常简单
 
2：LangChain包版本的问题

大概遇到以下一些问题：
 
> OpenAIEmbeddings Unsupported OpenAI-Version header provided: 2022-12-01

指定OpenAI版本：

```
OpenAIEmbeddings(openai_api_version='2020-11-07')
```

参考：https://github.com/hwchase17/langchain/issues/4154

> ERROR:root:'OpenAIEmbeddings' object has no attribute 'query_model_name'

降级版本解决：

```
pip install langchain==0.0.148
```

> ERROR:root:ChatVectorDBChain does not support async 

ChatVectorDBChain在某些版本不支持，可以在query_data.py中替换为ConversationalRetrievalChain

参考：https://github.com/hwchase17/chat-langchain/issues/51

在Windows下遇到以下问题：

> ModuleNotFoundError: No module named 'faiss.swigfaiss_avx2'

```
ln -s swigfaiss.py swigfaiss_avx2.py
```

参考：https://github.com/kyamagu/faiss-wheels/issues/39

最终使用的版本是langchain==0.0.148。

3：一点感想

这个仓库使用了很多优秀的技术，比如Streaming和Async，其中Streaming包括了StreamingLLMCallbackHandler和ChatVectorDBChain，而且常用的解决方案它都已经集成到LangChain。

看优秀的代码让人进步，惊叹代码编写能力，现在对LangChain的整体结构还是没掌握，所以看起来也挺吃力。