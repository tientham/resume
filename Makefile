all: index.html

index.html: minhtien-to.md views/layout.html
	./build.py minhtien-to.md index.html

.PHONY: clean

clean:
	rm -f *.html
