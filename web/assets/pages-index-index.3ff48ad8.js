import{r as a,s as t,o as e,c as l,w as o,i as s,a as u,b as d,d as r,I as n,e as c,f as i}from"./index-49ac3b8d.js";const m=((a,t)=>{const e=a.__vccOpts||a;for(const[l,o]of t)e[l]=o;return e})({data:()=>({host:"",mac:"",port:""}),methods:{submitForm(){a({url:"/api/wake",method:"POST",data:{host:this.host,mac:this.mac,port:this.port},success:a=>{this.result=a.data.message,1===a.data.code?t({title:a.data.msg,duration:1e3}):t({title:a.data.msg,icon:"error",duration:1e3})},fail:a=>{t({title:"请求失败",icon:"error",duration:1e3})}})}}},[["render",function(a,t,m,p,f,X){const _=r,h=n,V=s,g=c,b=i;return e(),l(V,{class:"container"},{default:o((()=>[u(V,{class:"form-group"},{default:o((()=>[u(V,{class:"input-group"},{default:o((()=>[u(_,null,{default:o((()=>[d("IP/域名:")])),_:1}),u(h,{modelValue:f.host,"onUpdate:modelValue":t[0]||(t[0]=a=>f.host=a),type:"text",placeholder:"请输入IP或域名"},null,8,["modelValue"])])),_:1}),u(V,{class:"input-group"},{default:o((()=>[u(_,null,{default:o((()=>[d("MAC地址:")])),_:1}),u(h,{modelValue:f.mac,"onUpdate:modelValue":t[1]||(t[1]=a=>f.mac=a),type:"text",placeholder:"请输入MAC地址"},null,8,["modelValue"])])),_:1}),u(V,{class:"input-group"},{default:o((()=>[u(_,null,{default:o((()=>[d("端口:")])),_:1}),u(h,{modelValue:f.port,"onUpdate:modelValue":t[2]||(t[2]=a=>f.port=a),modelModifiers:{number:!0},type:"number",placeholder:"请输入端口,默认为8"},null,8,["modelValue"])])),_:1}),u(V,{class:"input-group"},{default:o((()=>[u(V,{class:"tip"},{default:o((()=>[u(g,null,{default:o((()=>[d("MAC格式支持冒号分割或无分隔符，支持大小写，符合要求的格式如: ")])),_:1}),u(g,null,{default:o((()=>[d("XX:XX:XX:XX:XX:XX或XXXXXXXXXXXX")])),_:1})])),_:1})])),_:1}),u(b,{onClick:X.submitForm,class:"uni-btn"},{default:o((()=>[d("唤醒")])),_:1},8,["onClick"])])),_:1})])),_:1})}],["__scopeId","data-v-47b8dfdf"]]);export{m as default};
