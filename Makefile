APP_PATH = $(HOME)/community_management_backend

install-gunicorn:
	systemctl stop gunicorn.service || true
	@echo "Copying gunicorn.service to /etc/systemd/system/"
	@cp $(APP_PATH)/deployment/gunicorn.service /etc/systemd/system/
	systemctl enable gunicorn.service
	systemctl start gunicorn.service

restart-gunicorn:
	@systemctl restart gunicorn
	@echo "Restarting gunicorn"
	@systemctl status gunicorn | cat

install-nginx:
	@cp $(APP_PATH)/deployment/community_management_backend.conf /etc/nginx/sites-enabled/
	@echo "Copying community_management_backend.conf to /etc/nginx/sites-enabled/"
	systemctl restart nginx