.PHONY: build validate audit open deploy help

help:
	@echo "Workout OS — Build Commands"
	@echo "  make validate   — check source data/template for errors before building"
	@echo "  make build      — validate + build docs/"
	@echo "  make audit      — full pre-deploy check: build + validate docs/ + icon check"
	@echo "  make open       — open docs/index.html in browser"
	@echo "  make deploy     — push docs/ to GitHub Pages (requires git remote)"

validate:
	python3 scripts/validate.py

build: validate
	python3 scripts/build.py

audit: build
	python3 scripts/validate.py --dist
	@test -f src/icons/icon-192.png && test -f src/icons/icon-512.png \
		&& echo "  ok      Icons: icon-192.png and icon-512.png present" \
		|| (echo "  ERROR   Icons: missing src/icons/icon-192.png or icon-512.png" && exit 1)
	@echo "── Audit passed — docs/ is ready to deploy ──"

open:
	open docs/index.html

deploy:
	git add docs/ && git commit -m "build: deploy workout-os" && git push
