	
marcus_holmes on Dec 5, 2019 [–]

Because a dependency isn't a service. You're talking about dependencies as if they're standalone services that you consume. I think that's probably the predominant attitude at the moment, so sandboxing dependencies to turn them into (effectively) standalone services that you consume might work.
But I don't use dependencies like that. I'm mostly just importing useful functions from a library. Having to sandbox that function away from the rest of my code is not going to work. I'll end up copy/pasting the code into my project to avoid that.


	
danShumway on Dec 5, 2019 [–]

When we talk about sandboxing dependencies, we're talking about sandboxing at an API level, not an OS level -- in some languages (particularly memory-unsafe languages) that's difficult, but in general the intention isn't to put dependencies in a separate process; it's to restrict access to dangerous APIs like network requests.
Sandboxing might be something like, "I'm importing a function, and I'm going to define a scope, and within that scope, it will have access to these methods, and nothing else." Imagine the following pseudo-code in a fictional, statically typed, rigid langauge.

  import std from 'std';
  import disk from 'io';
  import request from 'http';

  //This dependency (and its sub-dependencies) can
  //only call methods in the std library, nothing else.
  //I can call special_sort anywhere I want and I *know*
  //it can't make network requests or access the disk.
  //All it can do is call a few core std libraries.
  import (std){ special_sort } from 'shady_special_sort';

  function save (data) {
    disk.write('output.log', data);
  }

  function safe_save (data) {
    if (!valid(data)) { return false; }
    save(data);
  }

  function main () {
    //An on-the-fly sandbox -- access to safe_save and request.
    (request, safe_save){
      save('my_malware_payload'); //compile-time error
      disk.write('output.log', 'my_malware_payload'); //compile-time error
      safe_save('my_malware_payload'); //allowed
    }
  }

We're not treating our dependencies or even our inline code as a service here -- we're not loading the code into a separate process or forcing ourselves to go through a connector to call into the API. We're just defining a static constraint that will stop our program from compiling if the code tries to do something we don't want, it's no different than a type-check.
The difference between this and pure static analysis is that static analysis isn't something that's built into the language, and static analysis tries to guess intent. Static analysis says, "that looks shifty, let's alert someone." An language-level sandbox says, "I don't care about the intent, you have access to X and that's it."

Even in a dynamic language like JS, when people talk about stuff like the Realms proposal[0][1], they're talking about a system that's a lot closer to the above than they are about creating standalone services that would live in their own processes or threads.

This kind of style of thinking about security lends itself particularly well to functional languages and functional coding styles, but there's no reason it can't also work with more traditional class-based approaches as well -- you just have to be more careful about what you're passing around and what has access to what objects.

  class Dangerous () {
    unsafe_write (data) {
       //unvalidated disk access
    }
  }

  class Safe () {
    public Dangerous ref = new Dangerous();
    safe_write (data) {
       validate(data);
       ref.unsafe_write();
    }
  }

  function main () {
    Dangerous instance = new Dangerous();

    (instance){
      //I've just accidentally given my sandbox
      //access to `unsafe_write` because I left
      //a property public.
    }
  }

Even with that concern, worrying about my own references is still way, way easier than worrying about an entire, separate codebase that I can't control.
[0]: https://github.com/tc39/proposal-realms

[1]: https://gist.github.com/dherman/7568885


One nice thing about a virtualenv is that you get a copy of the Python interpreter in there, so it is in fact a separate executable running, for the purposes of hanging the policies off of.

	
more-coffee on Dec 4, 2019 [–]

Depending on the platform, virtualenv defaults to creating a symlink to the Python executable. You can override it with --copies, but then you have a new problem: updating the interpreter in all virtualenvs when a new Python release comes out.

	
mikepurvis on Dec 4, 2019 [–]

On Ubuntu 16.04, the default behaviour is definitely to copy it, and there are no tricks with hardlinks or anything else:
    $ virtualenv foo
    Running virtualenv with interpreter /usr/bin/python2
    New python executable in /home/administrator/foo/bin/python2
    Also creating executable in /home/administrator/foo/bin/python
    Installing setuptools, pkg_resources, pip, wheel...done.

    $ ls -la foo/bin
    total 3464
    drwxrwxr-x 2 administrator administrator    4096 Dec  4 11:06 .
    drwxrwxr-x 7 administrator administrator    4096 Dec  4 11:06 ..
    -rw-rw-r-- 1 administrator administrator    2082 Dec  4 11:06 activate
    -rw-rw-r-- 1 administrator administrator    1024 Dec  4 11:06 activate.csh
    -rw-rw-r-- 1 administrator administrator    2222 Dec  4 11:06 activate.fish
    -rw-rw-r-- 1 administrator administrator    1137 Dec  4 11:06 activate_this.py
    -rwxrwxr-x 1 administrator administrator     252 Dec  4 11:06 easy_install
    -rwxrwxr-x 1 administrator administrator     252 Dec  4 11:06 easy_install-2.7
    -rwxrwxr-x 1 administrator administrator     239 Dec  4 11:06 pip
    -rwxrwxr-x 1 administrator administrator     239 Dec  4 11:06 pip2
    -rwxrwxr-x 1 administrator administrator     239 Dec  4 11:06 pip2.7
    lrwxrwxrwx 1 administrator administrator       7 Dec  4 11:06 python -> python2
    -rwxrwxr-x 1 administrator administrator 3492656 Dec  4 11:06 python2
    lrwxrwxrwx 1 administrator administrator       7 Dec  4 11:06 python2.7 -> python2
    -rwxrwxr-x 1 administrator administrator    2341 Dec  4 11:06 python-config
    -rwxrwxr-x 1 administrator administrator     230 Dec  4 11:06 wheel
This is with virtualenv 15.0.1.

	
more-coffee on Dec 7, 2019 [–]

Sorry for slow response, I don't check back here often enough.
You're right about virtualenv. I don't realy use that anymore, the venv module added in 3.3 gets the job done. And that does default to symlinks for posix. https://github.com/python/cpython/blob/3.8/Lib/venv/__init__...

