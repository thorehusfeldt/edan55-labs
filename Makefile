
DIRS    = collatz81 independentset 	maxcut 	pagerank

docs:
	mkdir docs
	for d in $(DIRS); do (cd $$d/docs; $(MAKE); mv *.pdf ../../docs; git clean -xfd); done

clean:
	git clean -xfd
