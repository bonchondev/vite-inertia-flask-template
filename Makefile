MAKEFLAGS+="-j 2"

FLASK_DEV=FLASK_APP="app:create_app('dev')" FLASK_DEBUG=1

init:
	pip install -r requirements.txt
	@pnpm --prefix "vite" install

dev-python:
	$(FLASK_DEV) flask run

dev-vue:
	@pnpm run --prefix "vite" build:dev

dev: dev-python dev-vue

prod-python:
	echo "You must implement your production service here"
	exit 1

prod-vue:
	@pnpm run --prefix "vite" build

prod: prod-vue prod-python
