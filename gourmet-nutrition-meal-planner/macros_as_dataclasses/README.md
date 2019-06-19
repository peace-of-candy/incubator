Gourmet Nutrition Meal Planner
===

This "solution" showcases the use of dataclasses to represent different macros
although it does not leverage that functionality it does illustrate a means
to represent macros while supporting arithmetic operations across them and
between them whilst simultaneously allowing for each to be decomposed further
into its constituent components, i.e., it would be trivial to extend the
carbohydrates class to render out its sugar- and fiber-content.

The actual planner is dumb, and does not take into account the design of
the recipes but simply aggregates the different macros of the different
meals that compose a given day.
