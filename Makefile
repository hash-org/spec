PRAC_NAME:=$(shell pwd | awk -F'/' '{ print $$(NF-1)"-"$$NF; }')

zip: report
	mkdir -p out/
	git archive -o out/"$(PRAC_NAME)".zip HEAD ./src
	cd report; zip -r ../out/"$(PRAC_NAME)".zip report.pdf

report: FORCE
	$(MAKE) -C report

FORCE: ;

.PHONY: clean
clean: 
	rm -rf out
