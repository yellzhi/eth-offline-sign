
### 安装配置
#### 安装依赖库
1. 安装python3
2. 安装web3 
   `$ sudo pip3 install web3`
3. 安装jsonrpc   
   `$ sudo pip3 install json-rpc`
   `$ sudo pip3 install Werkzeug`

#### 启动
   * 实例：
      `$ python3 ./singServer.py -i 127.0.0.1 -p 40002 -n 127.0.0.1:8801` 
     
   服务器启动地址为：127.0.0.1:40002   
   远程节点为：127.0.0.1:8801 (可以省略，省略后不能交易发送到节点，只能签名交易)      
   如果远程节点链接失败，那么 交易中的nonce不能自动获取，则需要在交易中指定
#### 接口
   `getAccount` : 创建账户  
   参数: num(int) 创建个数
   * 请求  
   `curl -X POST --data '{"jsonrpc":"2.0","method":"getAccount","params":[1],"id":1}'` 
   * 响应
   ```
   {
    "result": [
        {
            "address": "0x2b09857CDdc913B9708F065befac6836ebA42dAe",
            "privateKey": "0x378239427e204a5c6a8ef200c20d1bcdf89b11b0913615f6b2f12f2a92ca14ef",
            "bas58Key": "4jgbSiZM8m7jsKwpicVLe7Y5JTEYpWYRN9FeL1RusUaS"
        }
    ],
    "id": 2,
    "jsonrpc": "2.0"
}
   ```
* 说明：    
  address：账户地址    
  privateKey：账户私钥    
  bas58Key：base58编码的私钥
  #### sign 签名交易
   参数: json 交易json数据， key 账户私钥
   * 请求  
   ```
   curl -X POST --data '{
         "jsonrpc":"2.0",
         "method":"sign",
         "params":[
          "0x991de187e4bebc7467e4ce2c1365be6cd74199634e356eea45018458113e4c2d",
          {
            "chainId": 600, 
            "nonce": "0x1", 
            "from": "0x8Db0d0Dd0E1571c0d22F821fde96c7AF910A0b45",
            "to": "0x3789Ba57b337AA50F219DFDfbE62525f8CFA3b0c", 
            "gas": "0xfffff", 
            "value": 0, 
            "data": "", 
            "gasPrice": 100  
            }
         ],
         "id":1
      }'
  ``` 
   * 响应
   ```
   {
    "result": {
        "trasaction": {
            "chainId": 600,
            "nonce": "0x8",
            "from": "0x8Db0d0Dd0E1571c0d22F821fde96c7AF910A0b45",
            "to": "0x3789Ba57b337AA50F219DFDfbE62525f8CFA3b0c",
            "gas": "0xfffff",
            "value": 0,
            "data": "",
            "gasPrice": 100
        },
        "sign": "0xf8620864830fffff943789ba57b337aa50f219dfdfbe62525f8cfa3b0c80808204d4a02784e3634a91d717a22b3420df10af8b74807c8549e362ecb7623d3ebbd06a3aa003de87e9f007620bfbd4f7af74132171d3eae7a631516e22529305b09b679cad"
    },
    "id": 2,
    "jsonrpc": "2.0"
}
   ```
* 说明：    
  trasaction：交易原始数据    
  sign：交易签名数据    
  
#### signSend 签名交易
   参数: json 交易json数据， key 账户私钥
   * 请求  
   ```
   curl -X POST --data '{
         "jsonrpc":"2.0",
         "method":"signSend",
         "params":[
          "0x991de187e4bebc7467e4ce2c1365be6cd74199634e356eea45018458113e4c2d",
          {
            "chainId": 600, 
            "nonce": "0x1", 
            "from": "0x8Db0d0Dd0E1571c0d22F821fde96c7AF910A0b45",
            "to": "0x3789Ba57b337AA50F219DFDfbE62525f8CFA3b0c", 
            "gas": "0xfffff", 
            "value": 0, 
            "data": "", 
            "gasPrice": 100  
            }
         ],
         "id":1
      }'
  ``` 
   * 响应
   ```
   {
    "result": {
        "trasaction": {
            "chainId": 600,
            "nonce": "0x8",
            "from": "0x8Db0d0Dd0E1571c0d22F821fde96c7AF910A0b45",
            "to": "0x3789Ba57b337AA50F219DFDfbE62525f8CFA3b0c",
            "gas": "0xfffff",
            "value": 0,
            "data": "",
            "gasPrice": 100
        },
        "sign": "0xf8620864830fffff943789ba57b337aa50f219dfdfbe62525f8cfa3b0c80808204d4a02784e3634a91d717a22b3420df10af8b74807c8549e362ecb7623d3ebbd06a3aa003de87e9f007620bfbd4f7af74132171d3eae7a631516e22529305b09b679cad",
        "txHash": "0x4cb53ec51b5365bc9b843846fc624a7f4d1c033700b13da37e6184d83a6a6903"
    },
    "id": 2,
    "jsonrpc": "2.0"
   }
   ```
* 说明：    
  trasaction：交易原始数据    
  sign：交易签名数据    
  txHash：交易hash      
   
   **交易发送到了server启动是的node 地址的节点**
  
   
