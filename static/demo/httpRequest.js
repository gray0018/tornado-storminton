// import config from './config'
config ={
  // host:"http://manage.quickfs.com.cn"
  // host:"http://222.85.76.182:9092"
  host:"https://pmobile.zybank.com.cn:9090"
}

class HttpRequest {
  constructor () {
    // this.arg = ''
    // this.token = ''
    this._tokenRegister = {}
    this._tokenSeed = 0
    this._sessionId = ''
    this.class2type = {
      '[object Boolean]': 'boolean',
      '[object Number]': 'number',
      '[object String]': 'string',
      '[object Function]': 'function',
      '[object Array]': 'array',
      '[object Date]': 'date',
      '[object RegExp]': 'regExp',
      '[object Object]': 'object'
    }
  }

  requestData (maskShow, urlType, argData) {
    var arg = argData
    var data = arg.data
    var requestUrl = this.getrequestUrl(urlType)
    var token = this._tokenRegister[arg.id]
    if (!token) {
      token = this.getToken()
      this._tokenRegister[arg.id] = token
    }
    if (!data) {
      data = {}
    }
    var reqData = {
      body: data,
      header: {
        transCode: arg.id,
        time: new Date().getTime()
      }
    }
    var jsonStr = JSON.stringify(reqData)
    console.log('===>request:' + jsonStr)

    let a = {
      _$type: 'service',
      _$id: arg.id,
      _$service: arg.name,
      _$data: jsonStr,
      // _$sessionid: '31231231231231',
      _$token: token
    }
    let b = this.encode(a, 'application/x-www-form-urlencoded')
    console.log('xxxxxxxxxxxxxxxxxx:' + b)
    return new Promise((resolve, reject) => {
      // if (maskShow) {
      //   wx.showLoading({
      //     title: '加载中',
      //     mask: true
      //   })
      // }
      // wx.request({
      $.ajax({
        url: requestUrl,
        data: b,
        // header: {
        //   // 'content-type': 'text/plain;charset=UTF-8'
        //   'content-type': 'application/json;charset=utf-8'
        // },
        dataType: 'text',
        contentType:'application/json; charset=UTF-8',
        type: 'POST',
        success: function (res) {
          console.log(res)
          let result = JSON.parse(res)
          console.log("success:======")
          if ($(".change_qfs_code_btn").text()=="正在提交 请稍候"){
            $(".change_qfs_code_btn").text("更新")
            if (result["data"]["b"]["RetMsg"] == "SUCCESS"){
              Hs.change_qfs_code_action()
            }else{
              alert(result["data"]["b"]["RetMsg"])
              $(".send_sms").text("点击重发")
            }
          }else if ($(".login_btn").text()=="正在访问 请稍候"){
            $(".login_btn").text("点击开始访问")
            if (result["data"]["b"]["RetMsg"] == "SUCCESS"){
              Hs.reset_qfs_code_action()
            }else{
              alert(result["data"]["b"]["RetMsg"])
              $(".find_back_code").text("点击重发")
            }
          }

          // if (maskShow) {
          //   wx.hideLoading()
          // }
          // console.log('success:' + JSON.stringify(res))
          // resolve(res.data.data)
          resolve(res.data)
        },
        error: function (res) {
          console.log(res)
          console.log("error:======")
          alert("服务存注册失败")
          // if (maskShow) {
          //   wx.hideLoading()
          // }
          // wx.showToast({
          //   title: JSON.stringify(res),
          //   icon: 'none',
          //   duration: 7000
          // })
          // console.log('fail:' + JSON.stringify(res))
          reject(res.data)
        }
      })
    })
  }

  getToken () {
    this._tokenSeed += 1
    if (this._tokenSeed < 0) {
      this._tokenSeed = 0
    }
    var curData = new Date()
    var token = this._tokenSeed + '-' + curData.getTime()
    return token
  }

  getSessionId () {
    return new Promise((resolve, reject) => {
      var sessionId = this.readSessionId()
      if (sessionId) {
        resolve(sessionId)
      } else {
        var requestUrl = this.getrequestUrl(config.URL_ZYBANK)
        wx.request({
          url: requestUrl,
          method: 'POST',
          data: {
            _$type: 'options',
            _$actions: 'uuid'
          },
          success: function (res) {
            console.log('getSessionId-success:' + JSON.stringify(res))
            resolve(res)
          },
          fail: function (res) {
            console.log('getSessionId-fail:' + JSON.stringify(res))
            reject(res)
          }
        })
      }
    })
  }

  readSessionId () {
    if (this._sessionId === undefined) {
      this._sessionId = wx.getStorage({
        key: '$sessionId'
      })
    }
    return this._sessionId
  }

  getrequestUrl (urlType) {
    // console.log('config.URL_ZYBANK:' + config.URL_ZYBANK)
    // console.log('config.host:' + config.host)
    // console.log('config.AliHost:' + config.AliHost)
    // console.log('getrequestUrl:' + urlType)
    console.log(config.host + '/services/serviceInvoke')
    return config.host + '/services/serviceInvoke'
    // if (urlType === config.URL_ZYBANK ) {
    //   return config.host + '/services/serviceInvoke'
    // }else if (urlType === config.URL_ALI) {
    //   return config.AliHost + '/services/serviceInvoke'
    // }else {
    //   return config.host + '/services/serviceInvoke'
    // }

  }

  type(obj) {
    var toString = Object.prototype.toString;
    var t = toString.call(obj);
    return obj == null ? String(obj) : this.class2type[t] || "object";
  }

  encode(data, contentType) {
    if (contentType === void (0)) {
        contentType = "text"
    }
    contentType = contentType.trim().toLowerCase()
    //结果
    var res = ""
    if (contentType == "application/x-www-form-urlencoded") {
        //对象转换为form提交格式
        if (this.type(data) == "object") {
            for (var name_1 in data) {
                var value = data[name_1]
                //获取value数据类型
                var valType = this.type(value)
                if (valType == "array") {
                    for (var i = 0; i < value.length; i++) {
                        var item = name_1 + "=" + encodeURI(value[i])
                        if (res.length > 0) {
                            res += "&"
                        }
                        res += item
                    }
                }
                else {
                    var item = name_1 + "=" + encodeURI(value)
                    if (res.length > 0) {
                        res += "&"
                    }
                    res += item
                }
            }
        }
        else {
            res = data
        }
    }
    return res
  }
  
}
