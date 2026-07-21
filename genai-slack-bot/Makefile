reportDirectory=coverage

rwildcard=$(foreach d,$(wildcard $(1:=/*)),$(call rwildcard,$d,$2) $(filter $(subst *,%,$2),$d))
LAMBDAS := $(patsubst lambdas/%/src,%,$(call rwildcard,lambdas,*src))

all: $(LAMBDAS)

.PHONY: $(LAMBDAS)
$(LAMBDAS): clean lint test-libraries
	@echo "testing $@..."
	test -d venv || python -m venv venv
	. venv/bin/activate; python -m pip install -r lambdas/$@/src/requirements.txt ; python -m pip install --upgrade -r requirements.dev.txt
	. venv/bin/activate; coverageReport=$(reportDirectory)/$@/coverage/cobertura/cobertura-coverage.xml testResults=$(reportDirectory)/$@/coverage/junit/junit.xml covDir=lambdas/$@ testPath=lambdas/$@/src/test/unit bash ./scripts/test.sh $@
	touch venv/bin/activate

$(foreach lambda, $(LAMBDAS), $(eval $(lambda)-docker: clean ;\
	@echo "building $(lambda) for docker" ;\
	python -m pip install -r lambdas/$(lambda)/src/requirements.txt \
))
clean:
	/bin/rm -rf {lambdas,lib}/**/__pycache__/
	/bin/rm -rf {lambdas,lib}/**/htmlcov/
	/bin/rm -rf {lambdas,lib}/**/integration_test/__pycache__/
	/bin/rm -rf {lambdas,lib}/**/test/__pycache__/
	/bin/rm -f {lambdas,lib}/**/.coverage
	/bin/rm -f {lambdas,lib}/**/.*test.log
	/bin/rm -f {lambdas,lib}/**/build/*

devenv: requirements.dev.txt
	test -d devenv || python -m venv devenv
	. devenv/bin/activate; python -m pip install --upgrade -r requirements.dev.txt
	touch devenv/bin/activate

format: devenv
	@echo "Formatting"
	. devenv/bin/activate; black .

lint: devenv
	@echo "Linting"
	. devenv/bin/activate; python -m pylint .

test-libraries:
	@echo "Testing libraries"
	test -d venv || python -m venv venv
	. venv/bin/activate; python -m pip install -r lib/requirements.txt ; python -m pip install --upgrade -r requirements.dev.txt
	. venv/bin/activate; coverageReport=$(reportDirectory)/lib/coverage/cobertura/cobertura-coverage.xml testResults=$(reportDirectory)/lib/coverage/junit/junit.xml covDir=lib testPath=lib/test bash ./scripts/test.sh

.PHONY: all $(LAMBDAS) clean devenv format lint test-libraries

run:
	docker build --rm=false --build-arg appName=myapp --build-arg build=local --build-arg arch=amd64 -t myapp -f lambdas/chatbot/Dockerfile .
	docker run -p 9000:8080 --platform linux/amd64 myapp

test:
	docker build --rm=false --build-arg appName=myapp --build-arg build=local --build-arg lambdaHandler=chatbot_python.my_handler --build-arg arch=amd64 -t myapp .