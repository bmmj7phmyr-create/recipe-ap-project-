def test_update_recipe_assign_ingredient(self):
    """Test assigning an existing ingredient when updating a recipe."""
    ingredient = Ingredient.objects.create(user=self.user, name='Cilantro')
    recipe = create_recipe(user=self.user)
    recipe.ingredients.add(ingredient)

    ingredient2 = Ingredient.objects.create(user=self.user, name='chili')
    payload = {'ingredients': [{'name': 'chili'}]}
    url = detail_url(recipe.id)
    res = self.client.patch(url, payload, format='json')

    self.assertEqual(res.status_code, status.HTTP_200_OK)
    self.assertIn(ingredient2, recipe.ingredients.all())
    self.assertNotIn(ingredient, recipe.ingredients.all())



def test_clear_recipe_ingredients(self):
    '''test clearing a recipes ingredients'''
    ingredient=Ingredient.objects.create(user=self.user,name='carlic')
    recipe=create_recipe(user=self.user)
    recipe.ingredients.add(ingredient)

    payload={'ingredients':[]}
    url=detail_url(recipe.id)
    res=self.client.patch(url,payload,format='json')

    self.assertEqual(res.status_code,status.HTTP_200_OK)
    self.assertEqual(recipe.ingredients.count(),0)

