# reveal_rfp - Poverty vignette

This repository contains code for a Real Facts interactive web vignette on USA poverty. Basic layout as roughly as follows in screenshot below -- clickable slides with interactive visualizations and transitions based on user input. As tools, Javascript and D3.js are relied upon heavily to add the visualization and interactivity.

![Screenshot](assets/screenshot.png)

## To use:

1. `git clone https://github.com/wnowak10/reveal_rfp.git`
2.  Download and launch [MAMP](https://www.mamp.info/en/).
3. At MAMP open, click 'Start Servers' > 'Open WebStart Page' > 'My Website' and then navigate to `employment/` or whatever you titled this cloned directory. From there, click on `docs/` which contains source code to run this vignette in your browser. The start page should look like the slide screenshotted above. 

## `docs` README:

Repository structure borrowed from [Reveal.js](https://revealjs.com/#/). `index.html` contains references to individual slides, which are often (if not always) their own HTML pages with D3.js interactives...which are themselves stored in the `content` directory. 

This structure is inelegant, as changes to the site often require changes to both `index.html` and individual slides.

- `content/`: contains `data` and `slides` directories with key content for site.

- `index.html` - body HTML file, contains code for the 'script' of our HTML vignette.

- `js/` : A suite of JS libraries...to note, `reveal` contains functinality for reveal.js library...however, the start of the file also now contains some custom functionality to allow us to customize the behavior of the user's right arrow clicks. 

## How to's:

### How to add a slide?

To add a slide, we use to different methods (TO DO: what is/are the difference(s)?) add to `index.html`:


 .1. Add `<section>` with class name and then use JQuery to load.

```
$(function() {
	$(".<EXAMPLE>").load("content/slides/<EXAMPLE>/<EXAMPLE>")
			 }
  )
```
Followed by 

```
<section>
	<div class="<EXAMPLE>"></div>
</section>
```

 .2. Load directly.
 
```
<section>
<!-- D3 HTML files should be called with the following
     class and data-file attributes. -->
	<div class="fig-container" 
	data-file="content/slides/<EXAMPLE_D3_DIR>/index.html">
	</div> 	
</section>
```