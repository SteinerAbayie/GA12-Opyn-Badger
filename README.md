# GA12-Opyn-Badger

The project is an attempt to show how one may use Opyn's contracts to mint a covered call that can then be sold on Gnosis Safe, Airswap, Uniswap, or Ox.

Initially I wanted to use Lyra to sell the call options but there was a slight hiccup in that dev process. Right now Lyra is deployed on Optimism and 
only accepts sUSD. If one was to start with wBTC they would need to swap for lUSD bridge to Optimism then swap to sUSD then buy/sell the options. While a 
viable method, testing for this flow would be difficult. I did not identify an end to end flow for testing so this route was dropped.

### Running the code:

To run the Openvault.py you will need a .env with an ETHERSCAN_TOKEN,WEB3_INFURA_PROJECT_ID, and PRIVATE_KEY defined. All addresses will need to be for kovan.

Make sure you change KovanWallet_addr in Openvault.py 

Nothing needs to be changed to run gitproj.py, that script is intended to show how a swap on curve.fi could be done. wBTC -> sUSD.

### Things to be added:

Unit tests, integration tests, the ablity to sell the tokens in a test enviroment, integration with the badger strategy mix, diagrams showing the entire option flow. Figuring out how to price the options. I asked the dev channel on Opyn and it seems like the jury is still out on how to effectivly price the options. Figuring out how to set the strike price is also an interesting challenge, the 5-10% above current trading price seems best but with BTC IV who knows.


## Conclusion:

This was my **first** hackathon project, it was fun. Seeing how development is done in web3 was interesting and I learned a tok. If I could go back I would have started when the hackathon started and not 8ish days in, in my defence, I started as soon as I finished the freecodecamp solidity tutorial. I would have also spent more time finding team members, and I would have spend more time reading documentation and would've reached out to people on discord sooner. A big takeaway for myself has been that whoever solves the problem of getting new projects to clearly document their code is going to change the game and in the absence of clear documentation, Discord dev channels are your best friend. Also there should be more cross project collaboration. 

**If there are ways that this project could be improved, please let me know!**
