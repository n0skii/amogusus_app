# TAG="django_test_main"

# # sudo docker stop $(docker ps -aq)
# # sudo docker rm $(docker ps -a -q)

# sudo docker build . -t $TAG

# # sudo docker run -d -p 8000:8000 $TAG

# sudo docker tag $TAG n0skii/$TAG
# sudo docker push n0skii/$TAG

docker-compose down
docker-compose up --build -d
docker-compose run web python manage.py migrate
