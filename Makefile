DIRS    = collatz81 independentset 	maxcut 	pagerank	rainbow	marking treewidth

sources_docs := $(shell find -name "*.tex")
dir_docs := "docs"

docs: ${sources_docs}
	@# Create dir_docs if missing.
	@[ -d ${dir_docs} ] || mkdir docs
	@# Use symbolic links to avoid 'deleted: X.pdf' message in git, still
	@# 'modified' though.
	@for d in $(DIRS); do (cd $$d/docs; $(MAKE); ln -rs *.pdf ../../docs); done

clean:
	git clean -xfd

stage_tracked_pdfs:
	@# Iterate over all tracked+modified pdf and force add them."
	@for modified_file in $(shell git ls-files . -m); do\
		case "$$modified_file" in\
			*.pdf)\
				git add -f "$$modified_file";;\
		esac;\
	done

discard_tracked_pdfs:
	@# Discard changes to all tracked pdfs, will always appear as changed?
	@git checkout -- "*.pdf"
