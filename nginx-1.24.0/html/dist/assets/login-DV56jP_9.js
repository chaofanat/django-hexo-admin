import{_ as i,c as u,a as t,e as c,f as l,v as n,b as _,w as m,r as h,o as p,d as f}from"./index-DIsAfUU2.js";const v={data(){return{username:"",password:""}},methods:{login(){this.$axios.post("/api-auth",{username:this.username,password:this.password}).then(e=>{e.data.token?(localStorage.setItem("token",e.data.token),localStorage.setItem("username",e.data.username),localStorage.setItem("user_id",e.data.user_id),this.$axios.defaults.headers.common.Authorization="Token "+e.data.token,alert("用户"+e.data.username+"登录成功",{noresume:!0}),this.$router.push("/")):(alert("登录失败,用户名或密码错误"),console.log(e))}).catch(e=>{console.log(e),alert("登录失败,用户名或密码错误")})}}},x={class:"container"},b={class:"row"},w={class:"col-md-4 mx-auto"},g={class:"card mt-5"},k={class:"card-body"},y=t("h5",{class:"card-title text-center"},"用户登录",-1),F=t("hr",null,null,-1),B={class:"card-text"},V={class:"mb-3"},C=t("label",{for:"username",class:"form-label"},"用户名",-1),D={class:"mb-3"},S=t("label",{for:"password",class:"form-label"},"密码",-1),z=t("button",{type:"submit",class:"btn btn-primary"},"登录",-1),I=t("hr",null,null,-1),N={class:"text-left"};function T(e,s,q,A,a,r){const d=h("router-link");return p(),u("div",x,[t("div",b,[t("div",w,[t("div",g,[t("div",k,[y,F,t("div",B,[t("form",{onSubmit:s[2]||(s[2]=c((...o)=>r.login&&r.login(...o),["prevent"]))},[t("div",V,[C,l(t("input",{type:"text",class:"form-control",id:"username","onUpdate:modelValue":s[0]||(s[0]=o=>a.username=o),required:""},null,512),[[n,a.username,void 0,{lazy:!0}]])]),t("div",D,[S,l(t("input",{type:"password",class:"form-control",id:"password","onUpdate:modelValue":s[1]||(s[1]=o=>a.password=o),required:""},null,512),[[n,a.password,void 0,{lazy:!0}]])]),z],32),I,t("div",N,[_(d,{class:"text-secondary",to:"/register"},{default:m(()=>[f("还没有账号？")]),_:1})])])])])])])])}const U=i(v,[["render",T]]);export{U as default};
