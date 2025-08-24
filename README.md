# Test Assignment — Backend Department Sarafan

1. Write a program that outputs the first **n** elements of the sequence 122333444455555… (the number is repeated as many times as its value).

2. Implement a Django project for a grocery store with the following functionality:

* Ability to create, edit, and delete categories and subcategories of products in the admin panel.
* Categories and subcategories must have: name, slug, and image.
* Subcategories must be linked to their parent category.
* Endpoint for viewing all categories with subcategories, with pagination.
* Ability to add, edit, and delete products in the admin panel.
* Products must belong to a specific subcategory (and thus a category), and must include: name, slug, images in 3 sizes, price.
* Endpoint to display products with pagination. Each product output should include: name, slug, category, subcategory, price, list of images.
* Endpoint to add, update (change quantity), and delete products in the cart.
* Endpoint to display the contents of the cart with calculation of total quantity and total cost of items in the cart.
* Ability to fully clear the cart.
* Operations on category and product endpoints can be performed by any user.
* Operations on cart endpoints can only be performed by an authenticated user and only on their own cart.
* Token-based authentication must be implemented.

📌 The test assignment should be submitted as a link to your repository.
