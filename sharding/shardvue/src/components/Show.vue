<template>
    <div>
        <div align="center">
            <br>
            <h3>展示页面</h3>
            <br><br>
            <input type="text" placeholder="请输入查询内容" v-model="query_name">
            <input type="button" @click="query" value="确定">
            <br><br>
            <table>
                <tr>
                    <td>排名</td>
                    <td>客户端</td>
                    <td>分数</td>
                </tr>
                
                <tr v-for="message,index in messagelist">
                    <td>{{ index+1 }}</td>
                    <td>{{ message.name }}</td>
                    <td>{{ message.score }}</td>
                </tr>
                <tr>
                    <td>查询字段</td>
                </tr>
                <tr v-for="message,index in messagelist">
                    <td v-if="index in query_range">{{ index+1 }}</td>
                    <td v-if="index in query_range">{{ message.name }}</td>
                    <td v-if="index in query_range">{{ message.score }}</td>
                </tr>

            </table>
        </div>
    </div>
</template>
<script>
import axios from 'axios'
export default {
    data() {
        return {
            messagelist:[],
            query_name:'',
            query_range:[],
        }
    },
    mounted() {
        axios({
            url:'http://127.0.0.1:8000/order',
            method:'post',
        }).then((res)=>{
            if (res.data.code == 200){
                this.messagelist = res.data.messagelist
            }else{
                alert(res.data.message)
            }
        })
    },
    methods: {
        query(){
            let form_data = new FormData()
            form_data.append('query_name',this.query_name)
            axios({
                url:'http://127.0.0.1:8000/order',
                data:form_data,
                method:'post',
            }).then((res)=>{
				if (res.data.code == 200){
					this.query_range = res.data.query_range
				}else{
					alert(res.data.error)
				}
			})
        }
	
    },
}
</script>
<style>
    
</style>