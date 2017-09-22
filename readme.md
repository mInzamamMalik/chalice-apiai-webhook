clone and run command `pip install -r requirements.txt` then `chalice local` to run project locally


to deploy on aws just run command `chalice deploy`
note: if you add some extra dependency in the project dont forget to add those dependencies in `requirements.txt` file,
`requirements.txt` file in this case only supports `wheel` packeges, if you have `tarball` or some other packaging you have to build it manually and put in vendor folder according to Chalice documentation (http://chalice.readthedocs.io/en/latest/topics/packaging.html)