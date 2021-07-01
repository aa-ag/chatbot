# Chatbot 🤖

Small, fun project: building a chatbot.

### to run

- `conda create -n chatbot`
- `conda activate chatbot`
- `conda install django`
- `conda install channels`
- `conda install nltk`
- `docker run -p 6379:6379 -d redis:5`
- `conda install channels_redis`

#### test channel layer can communicate with Redis

```
$ python3 manage.py shell
>>> import channels.layers
>>> channel_layer = channels.layers.get_channel_layer()
>>> from asgiref.sync import async_to_sync
>>> async_to_sync(channel_layer.send)('test_channel', {'type': 'hello'})
>>> async_to_sync(channel_layer.receive)('test_channel')
{'type': 'hello'}
```

_see: https://channels.readthedocs.io/en/stable/tutorial/part_2.html_