# LOGR
Tool for viewing logs
developers' log console - listen on specified port and displays logs

Don't care anymore for setup many logfiles.

Supported protocols:
* `HttpGet` - preffered
* `JsonPost`

Test-it: `curl http://localhost:8080?logger=LOGR&level=DEBUG&message=Hello&time=12:12&app=APP1`

## Ussage
### 1) Start logr
`python main.py`

### 2) Configure your app
NLog config:

```xml
<target type='WebService'
    name='pat'
    url='http://localhost:8080'
    protocol='HttpGet'
    encoding='UTF-8'>
    <!-- MAGIC_FIELD is resolved via affiliation -->
    <parameter name="MAGIC_FIELD" type="System.String" layout="APP1"/>
    <parameter name="message" type="System.String" layout="${message}"/>
    <parameter name="logger" type="System.String" layout="${logger}"/>
    <parameter name="level" type="System.String" layout="${level}"/>
    <parameter name="time" type="System.DateTime" layout="${time}"/>
</target>
```

## How it works
1. HttpReader (GET/POST) -> LogRecord
2. Write LogRecord to all writers
3. File writer can assign file by `MAGIC_FIELD`


## Development

```sh
python -m venv ~/.virtualenvs/logr
source ~/.virtualenvs/logr/bin/activate

pip install termcolor
pip install aiohttp
pip install PyYAML
```