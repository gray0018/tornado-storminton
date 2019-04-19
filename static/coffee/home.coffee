root = exports ? this
# !!!! Hotpoor root object
root.Hs or= {}
Hs = root.Hs

root.start_logout = ()->
    redirect_uri = window.location.pathname + window.location.search
    window.location.href = "/api/logout?next="+ encodeURI(redirect_uri)
