// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Owner {


    address public owner;
    address private nOwner;


    constructor(){
        // require(_owner!=address(0),"Owner cannot be address 0");
        owner = msg.sender;
    }

    modifier onlyOwner(){
        require(msg.sender == owner);
        _;
    }
    modifier onlyNewOwner(){
        require(msg.sender == nOwner);
        _;
    }


    function transferOwnerShip(address _newOwner) public onlyOwner returns(bool){
        require(_newOwner!= address(0) && _newOwner!=owner,"error you suck");
        nOwner = _newOwner;
        return (true);
    }

    function transferOwnerShipAccept(bool _method) public onlyNewOwner returns(bool){
        if(_method == true){
            owner = nOwner;
            nOwner = address(0);
            return(true);
        }else{
            nOwner = address(0);
            return(false);
        }
    }
}

// storage jayii zakhire mishavad                     gas-> high
// memory : be hafeze mi ayad va paak mishavad        gas-> low
// calldata: data vared mishavad va pointer nadarad   gas-> low


contract sandoogh is Owner{

    mapping(address => uint) public userLevel;
    mapping(address => uint) public loanDist;
    mapping(address => uint) public blockMony;



    address[] public item;

    function invest() public payable{
        userLevel[msg.sender] += msg.value;
    }

    function withdrawal(uint _value, address payable _address) public {
        require(_value <= userLevel[msg.sender]-blockMony[msg.sender],"not enough fund in your account");
        userLevel[msg.sender] -= _value;
        _address.transfer(_value);
    }

    function loan(uint _value,address payable _borrower) public onlyOwner(){
        require(_value <= userLevel[msg.sender],"not enough fund in your account");
        loanDist[_borrower] += (_value * 12/10) ;
        blockMony[_borrower] +=  (_value * 12/10);
        _borrower.transfer(_value);
    }

    function repay() public payable{
        require(loanDist[msg.sender] <= msg.value);
        loanDist[msg.sender] -= msg.value;
        if (loanDist[msg.sender] == 0){
            blockMony[msg.sender] = 0;
        }
    }


    function extract()public onlyOwner(){
        payable(owner).transfer(address(this).balance);
    }

}

contract NFT is Owner {

    mapping(unit16 => address) public ownerNFT;
    mapping(uint16 => uint256) public nftSellPrice;


    unit16 public constant MAX_NFT = 10;
    unit256 public nftprice = 1 ether ;

    event NFTclaimed(address index nOwner ,unit16 indexed tokenid)

    modifier enoughMoney(){
        require(msg.sender.balance >= nftprice,"insufficient funds to claim NFT");
        _;
    }



    function buyNFT(uint8 _id) public payable enoughMoney() {
        payable(address(this)).transfer(nftprice);
        ownedNFT[_id] = msg.sender;
    }

    function transferNFT(uint _id,address _reciever) public {
        require(ownerNFT[_id] == msg.sender);
        ownerNFT(_id) = _reciever;
    }

    function prepareForSellNFT(uint8 _id,uint _price){
        require(ownerNFT[_id] == msg.sender);
        nftSellPrice[_id] = _price;
    }

    function buyNftFromReseller() {
    }



}