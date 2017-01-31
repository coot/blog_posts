# Loadin Content Message Using CSS3

CSS3 has `:empty` [pseudo
class](https://developer.mozilla.org/en-US/docs/Web/CSS/:empty) which can be
used to create loading icon before content arrives.  This works well with React
or other JavaScript frameworks which loads content into a DOM element.  For
a loading icon there the following requirements:

* show only if loading takes more than 300ms (that's arbitrary) - it's
  important not to show it too early, to not flash content for content that
  loads quickly
* should appear gradually with changing opacity

That's possible without any JavaScript (even without setting css classes on the
container).  Let assume that our app loads into:

```html
<main id="app"></main>
````

Then we can use the following snipet to set a loading message:

```css

#app:empty:after {
  content: "loading...";
  opacity: 0;
  animation: 500ms linear 300ms 1 forwards show;
}

@keyframes show {
 from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
```

And that's it - well you might like to add style it to your taste...

The `opacity: 0` hides the message, while the `animation-fill-mode: forwards`
will make it visible after the opacity animation has finished.  The animation
has a `300ms` delay and `animation-iteration-count: 1` will assure that it is
uncovered only once.

Note that the `#app` element has to be empty, i.e. cannot contain any node.  For examples
```
<main id="app">
</main>
```
contains a single text node and thus is not empty.

You can also use `#app:empty:before` to add a spinner icon.
