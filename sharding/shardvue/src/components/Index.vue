<template>
  <table align="center">
    <br><br>
    <input type="text" placeholder="请输入客户端" v-model="client">
    <br>
    <input type="text" placeholder="请输入分数" v-model="score">
    <br>
    <input type="button" @click="upload" value="提交">
  </table>
</template>

<script>
import axios from 'axios'
export default {
  name:'Index',
  data () {
    return {
      client:"",
      score:"",
    }
  },
  methods: {
    upload(){
			let form_data = new FormData()
			form_data.append('client',this.client)
			form_data.append('score',this.score)
			axios({
				url:'http://127.0.0.1:8000/index',
				method:'post',
				data:form_data,
			}).then((res)=>{
				if (res.data.code == 200){
					this.$router.push({'path':'show'})
				}else{
					alert(res.data.message)
				}
			})
		}
  },
  
}
</script>

<style>

</style>                                                         