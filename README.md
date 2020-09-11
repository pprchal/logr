# LOGR
Tool for viewing logs
developers' log console - listen on specified port and displays logs

### Ussage
## 1) Start

## 2) NLog config
```xml
<target type='WebService'
    name='pat'
    url='http://localhost:8080'
    protocol='JsonPost'
    encoding='UTF-8'>
    <parameter name="message" type="System.String" layout="${message}"/>
    <parameter name="logger" type="System.String" layout="${logger}"/>
    <parameter name="level" type="System.String" layout="${level}"/>
    <parameter name="time" type="System.DateTime" layout="${time}"/>
</target>
```

## packages
```
pip install termcolor
```