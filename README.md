# jetbrains-currencyconverter

Solution to JetBrains Academy Python Core project

Fetches up-to-date exchange rates rates in json format from https://floatrates.com

Takes user input (start currency, finish currency, start value) and calculates output value.

For each currency requested the program fetches the necessary data from a local cache (python dictionary), or else fetches the data from the website and adds it to the cache.
