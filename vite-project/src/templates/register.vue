<template>
  <div class="container">
    <div class="row">
        <div class="col-md-4 mx-auto">
            <div class="card mt-5">
                <div class="card-body">
                    <h5 class="card-title text-center">用户注册</h5>
                    <hr/>
                    <div class="card-text">
                      <form @submit.prevent="register">
                        <div class="mb-3">
                            <label for="username" class="form-label">用户名</label>
                            <input type="text" class="form-control" id="username" v-model.lazy="username" required>
                        </div>
                        <div class="mb-3">
                            <label for="email" class="form-label">电子邮箱</label>
                            <input type="email" class="form-control" id="email" v-model.lazy="email" required>
                        </div>
                        <div class="mb-3">
                            <label for="password" class="form-label">密码</label>
                            <input type="password" class="form-control" id="password" v-model.lazy="password" required>
                        </div>
                        <button type="submit" class="btn btn-primary">注册</button>
                    </form>
                  </div>
                </div>
            </div>
        </div>
    </div>
</div>
</template>
<script lang="ts" >
export default {
    name: 'Register',
    data() {
        return {
            username: '',
            email: '',
            password: ''
        }
    },
    methods: {
        register() {
            this.$axios.post('/register', {
                username: this.username,
                email: this.email,
                password: this.password
            }).then(res => {
                alert(res.data.username+'注册成功')
                this.$router.push('/login')
                console.log(res)
            }).catch(err => {
                alert('注册失败,用户名已经存在')
            })
        }
    }
}

</script>
<style>

</style>