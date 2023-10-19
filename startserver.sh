python3 manage.py collectstatic --noinput
python3 manage.py makemigrations
python3 manage.py migrate
docker-compose build
docker-compose up
exit 0
