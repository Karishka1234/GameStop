# Created by HP at 3/20/2020
Feature: Shopping Cart

 Scenario: User is able to add an item to the Shopping Cart
  Given Open https://www.gamestop.com/ page
  When Insert the outer worlds in search field
  And On search results page choose something and click it
  And Add product to shopping cart
  Then Expected product would be in cart
  And Close all pop-ups

  Scenario: User is able to add multiple items to the Shopping Cart
   Given Open https://www.gamestop.com/ page
   When Insert the outer worlds in search field
   And On search results page choose something and click it
   And Add product to shopping cart
   And Return to product search page
   And On search results page choose another product and click it
   And Add product to shopping cart
   Then Expected products would be in cart
   And Close all pop-ups


 Scenario: Shopping cart - Change quantity
   Given Open https://www.gamestop.com/ page
   When Insert the outer worlds in search field
   And On search results page choose something and click it
   And Add product to shopping cart
   And Click cart icon
   Then Close all pop-ups
   And Change quantity from 1 to 2
   Then Expected items in cart will be 2
