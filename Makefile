APP_PATH = $(HOME)/community_management_backend

install-gunicorn:
	sudo ln -s $(APP_PATH)/deployment/gunicorn.service /etc/systemd/system/
	systemctl enable gunicorn.service
	systemctl start gunicorn.service

gunicorn:
	systemctl restart gunicorn
	systemctl status gunicorn | cat

nginx-update:
	sudo ln -s $(APP_PATH)/deployment/community_management_backend.conf /etc/nginx/sites-enabled/
	sudo systemctl restart nginx