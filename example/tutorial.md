# Interactive rst tutorial
Welcome to the in depth rst tutorial! This tutorial is designed to be run
interactively, guiding you through the requirements gathering, detailed
design phase, and implementaiton of a project -- as well as fixing issues
that might come up.

In order to follow along, you must have rst installed somewhere on your PATH.
Check out the [User Guide](https://github.com/vitiral/rst/wiki/User-Guide)
for instructions.

Note: every time `rst tutorial ...` gets called it will delete the files it
created. This is so that it can update the files to be interactive. If you are
taking notes or creating other artifacts, you should do so in separate files
than the ones created, or use revision control like git as you progress
(recommended).

--------------------------------------------------
## Tutorial Stage 1: follow along document
Just run `rst tutorial` and read the created `tutorial.toml` file that
is created. This will give you an overview of rst syntax and how to write
artifacts.

--------------------------------------------------
## Tutorial Stage 2: high-level requirements and design specifications
> **Run `rst tutorial 2` to reset the local directory to this stage**

A few changes have been made to your local directory:
 - `tutorial.toml` has been removed
 - the `flash_card_challenge.htm` file has been added
 - the `design/` folder has been added with `purpose.toml` and `high_level.toml`
     in it
 - `.rst/settings.toml` has been updated with a new `artifact_paths`

Open `flash_card_challenge.htm` in a browser (or go
[here](http://wiki.openhatch.org/Flash_card_challenge))
and skim through the project that we will be executing. Don't worry! You don't
need to know python to follow along with this tutorial.

Now open `design/purpose.toml`. This is a rough attempt to translate the ideas
in `flash_card_challenge.htm` into purpose statements.

Purpose statements are important because they document why your project even
exists -- something that is important to know as you develop it! Without
high-level requirements, it is easy to loose sight of what your project is
trying to accomplish and can be difficult to keep track of which features are
useful and which are not.

In addition, purpose statements allow you to specify what your project will
accomplish, but then complete it in pieces. **rst** will help you track which
part is complete!

> ### Exercise 1:
> Review `design/purpose.toml` and make sure it makes sense. Does this
> accurately summarize the application we are trying to build? Are there any
> purpose requirements missing?

Now open `high_level.toml` in the same directory. This is mostly the high-level
specifications and requirements of the command/program itself.

High-level specifications allows you to lay out your ideas for how a project
should be approached before you actually write any code. It also allows you to
write out "TODOs" that you think **should** be done, but you maybe won't get
done in your minimum viable product.

> ### Exercise 2:
> Review the `design/high_level.toml` document. Which items do you think should
> be done immediately, and which will have to wait?

Now run:
```
    rst ls
```

This displays all the artifacts you just looked at, but colorizes them according
to whether they are complete or not. Right now, nothing is done so all you
see is red.

Now run:
```
    rst ls REQ-cmd -l
```

This calls to list only one artifact (REQ-cmd), and displays it in the "long"
format (`-l`)

Try `rst ls purpose -p` to search for all items with "purpose" in the name, you
can see that three purpose requirements appear.

> ### Exercise 3:
> Play around with the `rst ls` command a little more to get used to it, we will
> be using it a lot. Get help with:
> ```
    rst ls -h
```

Once you are done, continue onto stage 3.


--------------------------------------------------
## Tutorial Stage 3: detailed design and test design of the loading function
> **Run `rst tutorial 3` to reset the local directory to this stage**

A few changes have been made to your local directory:
 - `design/load.toml` has been created

> ### Exercise 1:
> Read through `design/load.toml` and see if the general plan makes sense to
> you. What would you change? Feel free to make any edits you think should be
> made. You can always return it to it's original state with `rst tutorial 3`

The first task we are going to address is how we load the questions into
the program. This is all defined under SPC-load. Run:
```
    rst ls SPC-load -l
```

From there you can see the parts that have to be implemented for SPC-load
to be considered done. Note that SPC-LOAD was auto-created because it is a
parent of other artifacts.

> ### Exercise 2:
> Explore each part of SPC-LOAD using the `rst ls` cmd.

`load.toml` details quite a bit of the design specifications, risks and tests
in order to implement this project. Let's actually get to work and start
coding.


--------------------------------------------------
## Tutorial Stage 4: writing and linking code
> **Run `rst tutorial 4` to start this stage of the tutorial**

A few changes have been made to your local directory:
 - `flash/` has been created with two files, `__init__.py`
     and `load.py`
 - `.rst/settings.toml` was updated to include the `code_paths` variable

> Note: for python, a directory with an `__init__.py` file is called a "module"
> and is python's packaging mechanism.

Take a look at `flash/load.py`, which contains the machinery for loading the
flash-cards file. Notice the various `#SPC-...` tags located in the
documentation strings. These tags are how rst knows which artifacts are
implemented and where. If an artifact is implemented in code in this way it is
marked as 100% "completed".

 - if it is a SPC or TST is tagged in the source code it is 100% done
 - otherwise it is as done as the average of it's parts

Additionally, an artifact is only considered "tested" when it's TST parts are
considered done.

Run the command

    rst ls SPC-load-format

Notice that it is now "implemented-at" `flash/load.py`. Go to where it says it
is implemented and confirm that the information is correct.

Head to `flash/tests/test_load.py` and notice that similar tags can be found
there for TST artifacts.

### Exercises
 1. run `rst ls ARTIFACT` on an artifact that is tagged in source. Now change
    the tag so that it is mispelled and run it again. Did the completeness
    change?
 2. do the same thing for an arifact in the `partof` field for a file in
   `design/`. Notice that invalid names blink red on your terminal and you get
    WARN messages. You can use this feature to help you ensure your artifact
    links are correct.
 3. we will be learning about `rst check` in the next step. Try it now with
    the changes you've made


--------------------------------------------------
## Tutorial Stage 5: handling errors
> **Run `rst tutorial 5` to start this stage of the tutorial**

A few changes have been made to your local directory:
 - `design/load.toml` has been changed to have a bunch of errors
 - `src/load.py` has been changed to include a few errors as well.

So far in the tutorial things have been done correctly -- but what if you
are new, or what if you have to refactor?

Here we are in the middle of refactoring our code and requirements a bit... but
we've messed some things up. It's your job to fix them. How to begin?

First of all, we can use what we already know. `rst ls` can help a lot for
refactors. It can answer the question "why is that REQ at 0%? It is implemented
somewhere!"

Well, let's try it for this project:

```
    # note: -OD displayes "partof | defined-at" instead of "parts | defined-at"
    rst ls -OD
```

Holy errors batman, That's a lot of red!

We can see that `rst ls` is not the right tool for the job -- from looking at
the number of errors, it would be very difficult to know where we need to
start. `rst check` is the command we want. It analyzes your project for
errors and displays them in a way that makes them easier to fix. Some of
the errors it finds are:

 - invalid `partof` fields: if you've renamed (or misspelled) an artifact but
    forgot to update artifacts that were parts of it, this will help you.
 - dangling locations in code: you might THINK writing `#SPC-awesome-func`
    in your code links to something, but unless that spec actually exists
    it isn't doing anything. `rst check` has your back.
 - recursive links: rst's completeness algorithm doesn't work if there are
    recursive partof links (i.e. A is partof B which is partof A)
    `rst check` will help you narrow down where these are comming from.
 - hanging artifacts: if you've written a SPC but haven't linked
    it to a REQ, then you probably want to (otherwise what exactly are you
    specifying?). The same goes for tests that are not testing any specs or
    risks.

> ### Exercise:
> use `rst check` to find errors and fix them. Keep running `rst check` and
> fixing errors until there are no errors, then run `rst ls` to see if the
> current status makes sense.

--------------------------------------------------
## Documenting your own project
To start documenting your own project, run `rst init` in your project and edit
`.rst/settings.toml` with the paths on where to find your code-implementations
and documents.


--------------------------------------------------
## Additional Resources

The wiki for rst, which contains additional resources and links,
can be found here:
    https://github.com/vitiral/rst/wiki

The developer of rst is also writing a book on quality best practices for
developers. It is highly recommended you check it out. It is currently a rough
draft, but it can already be a valuable resource for developers looking to
further the quality of the software they develop. Suggestions and comments
would be wonderful.

The book is and will always remain free and can be found at:
    https://vitiral.gitbooks.io/software-quality-for-developers/content/

The repository for the book is hosted here:
    https://github.com/vitiral/quality-book

--------------------------------------------------
## Summary and Final Words

Here are a few parting words of advice:

 1. Even when using requirements, you should still write a good README and other
      documentation for your users -- requirements SHOULD be used for bringing
      developers of your project up to speed but they aren't the best format for
      general users.
 2. Keep your artifacts fairly high level -- don't try to design every detail
      using rst. Using rst does not mean that you shouldn't use code comments!
 3. Use `rst ls` and `rst check` often, and fix those error messages!
 4. Keep names short and simple. Avoid unnecessary nesting. If you have web and
      cmdline ui elements, consider naming them just `REQ-web` and `REQ-cmd`
      instead of `REQ-ui-web` and `REQ-ui-cmd`. Trying to nest too deep can
      quickly get confusing.
 5. Don't be afraid to refactor your artifacts. It is actually easier than it
      might sound, as rst will help you find broken links and incomplete
      items in real time. Not to mention that if you use revision control
      (you should), your artifacts can be tracked with your project -- no more
      having your documentation and your code be wildly out of sync!

This tutorial took you part of the way through developing a simple project using
rst. I leave it as an exercise for the reader to finish the project in whichever
language you are most comfortable. Have some fun with the rst tool, try to break
it. If you find bugs or have any suggestions, please open a ticket at:
https://github.com/vitiral/rst/issues

Good luck!
