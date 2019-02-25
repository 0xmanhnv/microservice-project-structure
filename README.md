# microservice-project-structure
Improved Flask project structure for apis


### Problem 1: Too many nested levels
- [x] Extract all abstract classes into /core, hence can be navigated easily
    ```
    eg:
        from src.core.view import BaseView
        from src.core.model import BaseModel
    ```
- [x] Move all test configurations into /tests/test_helper.py
    ```
    since there are not much configurations and it also includes unittest only,
    it is unnecessary to have a directory just for that.
    ```
- [x] Move /factories out of the app
    ```
    factories should be held in one place only for easy navigate
    eg: from test.factories.account import Account, GuestAccount
    ```
- [x] Change /utility into utils.py
    ```
    namespace is not need for utilities and does making import easily becoming messy,
    hence, change into a file instead.
    ```
### Problem 2: Duplicated CRUD operation
- [x] Implement CRUD mixin for BaseModel

### Problem 3: Difficult to add Swagger doc as well as show urls
- [x] Move **/urls.py into **/views since encapsulation makes it less convenience
    ```
    urls can be show via Swagger, hence it eliminates the need of urls.py
    ```
- [x] Switch to flask_restplus from flask_restful since it provides better support for Swagger
    ```
    to show all routes of a blueprint, navigate it with postfix '/doc/
    eg: ../api/sample/doc/
    ```

### Problem 4: Test using development environent
- [x] Config test envinroment separately
    ```
    def create_app(self):
        env = 'unittest'
        app = create_app(env)
        ...
    ```

### Problem 5: Overusing __init__.py
- [x] Extract all logic inside __init__.py and provide better file name

### Problem 6: Global error handling with ability to customize
    TODO...


### TODO:
- [ ] Add proxies
- [ ] Add dynaconf
- [ ] Add docker
- [ ] Add sample CRUD
- [ ] Add sample testing
- [ ] Add dev.py.orig templates
- [ ] Add README construction
- [ ] Change `core` into `cores`
