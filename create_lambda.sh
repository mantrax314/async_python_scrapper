mkdir package
cp lambda_function.py package/
cp main.py package/

cp -r model package/

pip3.11 install -r requirements.txt -t package/


cd package
zip -r lambda_function.zip *
cd ..
mv package/lambda_function.zip .
rm -rf package