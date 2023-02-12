<template>
    <div id="wrapper">
    </div>
</template>

<script>
import axios from 'axios'
export default {
    data: () => ({
        html: '<h2>内容を取得できませんでした。</h2>',
    }),
    mounted: async function(){
        try{
            // 取得api
            let response = await axios.get('aboutHtml',{
                'withCredentials':true
            }).then(function(res){
                return res
            }).catch(function(error){
                return false;
            });
            if(response.status == 200){
                this.html = response.data[0].html;
            }
            let wrapper = document.getElementById('wrapper');
            wrapper.innerHTML = this.html;
        } catch(err) {
            this.debugConsole = err;
        }
    },
}
</script>