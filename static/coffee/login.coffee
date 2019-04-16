root = exports ? this
# !!!! Hotpoor root object
root.Hs or= {}
Hs = root.Hs

root.start_login = ()->
    $.ajax
        url: "/api/login"
        data:
            username: $("#login_account").val()
            password: $("#login_pwd").val()
        dataType: 'json'
        type: 'POST'
        success: (data)->
            console.log data
            if data.info == "success"
                if data.action == "redirect"
                    redirect_uri = data.redirect_uri
                    window.location.href = redirect_uri
        error: (data)->
            console.log data

# root.start_logout = ()->
#     $.ajax
#         url: "/api/logout"
#         data:
#             logout_account:
