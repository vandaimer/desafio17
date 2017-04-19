D=docker
IMAGE=desafio
DIR=$(CURDIR)

all:
	$(MAKE) build
	$(MAKE) run

build:
	$(D) build -t $(IMAGE) $(DIR)

run:
	$(D) run -it --rm -p 5000:5000 $(IMAGE)
