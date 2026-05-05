.PHONY: create-practice remove-practice

create-practice:
ifndef NAME
	$(error NAME is not defined)
endif
	if not exist "$(NAME)" mkdir "$(NAME)"
	copy PracticeMakefile "$(NAME)\Makefile"

remove-practice:
ifndef NAME
	$(error NAME is not defined)
endif
	if exist "$(NAME)" rmdir /S /Q "$(NAME)"