import{y as i,J as c}from"./index-B00xg2jH.js";import{_ as m,c as g,a as s,d as a,b as r,w as h,f as u,v as _,r as f,o as p}from"./index-BB5KvXD5.js";const v={name:"HexoConfig",data(){return{config:"",jsonconfig:""}},created(){this.$axios.defaults.headers.common.Authorization="Token "+localStorage.getItem("token"),this.$axios.get("/hexo_config").then(t=>{console.log(t.data.config),this.config=i.dump(c.parse(t.data.config))}).catch(t=>{console.log(t),console.log(localStorage.getItem("token"))})},methods:{parse(){try{this.jsonconfig=this.jsonstotring(c.stringify(i.load(this.config),null,2))}catch{alert("yml配置存在问题！")}},update(){this.parse(),this.$axios.post("/hexo_config",{config:this.jsonstotring(c.stringify(i.load(this.jsonconfig)))}).then(t=>{t.data.message!="success"?alert("保存失败:"+t.data.message):alert("配置已上传至服务器")}).catch(t=>{alert("保存失败:"+t)})},jsonstotring(t){return t=t.replace(/(\w+)\s*:/g,'"$1":'),t=t.replace(/"http"/g,"http").replace(/"https"/g,"https"),t=t.replace(/"mailto":name@email.com/g,"mailto:name@email.com"),t=t.replace(/(\d{1,3})\.(\d{1,3})\.(\d{1,3})\."(\d{1,3})"/g,"$1.$2.$3.$4"),t=t.replace(/"HH":"mm":ss/g,"HH:mm:ss"),t=t.replace(/\'/g,'"'),t}},mounted(){}},x={class:"container vh-100"},b={class:"row"},y={class:"col-md-2 vh-100"},k={class:"card h-100"},j={class:"card-body p-2"},w={id:"sidebarMenu",class:"d-flex flex-column align-items-start p-0 bg-light"},C=s("span",{class:"bi bi-card-list me-1"},null,-1),F={class:"nav nav-pills flex-column mb-auto"},D=s("li",{class:"nav-item"},[s("a",{class:"nav-link",href:"#"},[s("span",{class:"d-flex align-items-center"},[s("span",{class:"bi bi-collection me-1"}),a(" hexo配置 ")])])],-1),E={class:"nav-item"},$={class:"nav-item"},B={class:"col-md-10 vh-100"},H={class:"row row-cols-1 row-cols-md-2 h-100 g-4"},V={class:"col"},N={class:"card h-100"},T={class:"card-body p-4 h-100"},A={class:"d-flex justify-content-between align-items-center"},I=s("div",{class:"fs-5"},"hexo配置",-1),J=s("hr",{class:"my-3"},null,-1),M={class:"col"},S={class:"card h-100"},U={class:"card-body p-4"},W={class:"d-flex justify-content-between align-items-center"},z=s("div",{class:"fs-5"},"yml配置json格式预览",-1),q=s("hr",{class:"my-3"},null,-1);function G(t,e,K,L,n,l){const d=f("router-link");return p(),g("div",x,[s("div",b,[s("div",y,[s("div",null,[s("div",k,[s("div",j,[s("nav",w,[C,a(" 导航栏 "),s("ul",F,[D,s("li",E,[r(d,{class:"nav-link",to:"/hexo_theme"},{default:h(()=>[a("主题配置")]),_:1})]),s("li",$,[r(d,{class:"nav-link",to:"/"},{default:h(()=>[a("回到主页")]),_:1})])])])])])])]),s("div",B,[s("div",H,[s("div",V,[s("div",N,[s("div",T,[s("div",A,[I,s("div",null,[s("button",{class:"btn btn-primary",onClick:e[0]||(e[0]=o=>l.parse()),type:"button"}," 预览 ")])]),J,u(s("textarea",{class:"form-control h-75","aria-label":"With textarea",onChange:e[1]||(e[1]=o=>l.parse()),"onUpdate:modelValue":e[2]||(e[2]=o=>n.config=o)},null,544),[[_,n.config]])])])]),s("div",M,[s("div",S,[s("div",U,[s("div",W,[z,s("div",null,[s("button",{class:"btn btn-primary",onClick:e[3]||(e[3]=o=>l.update()),type:"button"}," 保存 ")])]),q,u(s("textarea",{class:"form-control h-75","aria-label":"With textarea","onUpdate:modelValue":e[4]||(e[4]=o=>n.jsonconfig=o)},null,512),[[_,n.jsonconfig]])])])])])])])])}const Q=m(v,[["render",G]]);export{Q as default};