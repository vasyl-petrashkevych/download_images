# download_images
Download all images of post pages or custom posts types from WordPress rest api
## How to use
1. Install python and requests library
    ```shell
    pip install requests
    ```
2. Open file ``index.py`` and change ``URL`` on yours
    ```
    URL = "https://yoursite.com/wp-json/wp/v2/[pages, posts, custom post type]?_embed"
   ```
3. Run the script Done

### NOTE!
Make sure that your custom post type is showing in rest read the [documentation](https://developer.wordpress.org/rest-api/extending-the-rest-api/adding-rest-api-support-for-custom-content-types/)