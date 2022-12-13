bigsmall:
	python3 main.py element-size --color-range light_yellow --output ./test_output ./assets/bottom-shape-coloring-page.jpg
	python3 main.py element-size --color-range light_yellow --small true --output ./test_output ./assets/bottom-shape-coloring-page.jpg
	python3 main.py video-processor --color-range white --output ./test_output ./assets/frutas.mp4

color-run:
	python3 main.py color-segment --color-range green --light-color true --output ./test_output ./assets/pecas_lego.jpg

gt-all:
	python3 main.py segment-image ./assets/ground_truth/01.jpg --gt ./assets/ground_truth/gt01.png --output ./test_output
	python3 main.py segment-image ./assets/ground_truth/02.jpg --gt ./assets/ground_truth/gt02.png --output ./test_output
	python3 main.py segment-image ./assets/ground_truth/03.jpg --gt ./assets/ground_truth/gt03.png --output ./test_output
	python3 main.py segment-image ./assets/ground_truth/04.jpg --gt ./assets/ground_truth/gt04.png --output ./test_output
	python3 main.py segment-image ./assets/ground_truth/05.jpg --gt ./assets/ground_truth/gt05.png --output ./test_output
	python3 main.py segment-image ./assets/ground_truth/06.jpg --gt ./assets/ground_truth/gt06.png --output ./test_output
	python3 main.py segment-image ./assets/ground_truth/07.jpg --gt ./assets/ground_truth/gt07.png --output ./test_output

morph-all:
	python3 main.py morph-op ./assets/morphology/01.png --struct_el "cross" --open_close "false" --output ./test_output
	python3 main.py morph-op ./assets/morphology/02.png --struct_el "cross" --open_close "false" --output ./test_output
	python3 main.py morph-op ./assets/morphology/03.png --struct_el "rect" --open_close "true" --output ./test_output
	python3 main.py morph-op ./assets/morphology/04.png --struct_el "rect" --open_close "true" --output ./test_output
