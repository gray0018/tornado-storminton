coffee -c -o static/js static/coffee
python web.py

# sed -i "" "s#^dev_type_now=.*#dev_type_now=\"online\"#g" dev_type.py
# rsync -avz . ubuntu@XXX.XXX.XXX:~/AIM_FOLDER/
# sed -i "" "s#^dev_type_now=.*#dev_type_now=\"local\"#g" dev_type.py