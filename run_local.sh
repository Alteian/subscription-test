if ! [ -f .local ]; then
echo "Create env file from sample" && exit
fi

docker-compose -f docker-compose.local.yml build

case "$1" in
"run")
    docker-compose -f docker-compose.local.yml run web python manage.py runserver
    ;;

"migrate")
    docker-compose -f docker-compose.local.yml run web python manage.py migrate
    ;;

"makemigrations")
    docker-compose -f docker-compose.local.yml run web python manage.py makemigrations
    ;;

*)
    docker-compose -f docker-compose.local.yml up
    ;;

esac
