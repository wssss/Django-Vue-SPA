<template>
    <div class="widget twitter">
        <h3 class="title">Tags</h3>
        <ul class="entry">
            <li v-for="tag in tags"><a href="#">{{tag.name}}</a><small>2</small></li>
        </ul>
    </div>
</template>
<script>

export default{

    created(){
        this.getTags();
    },
    data(){
        return {
            tags:[]
        }
    },
    methods:{
        getTags(){
            this.$http.get('api/post/tags')
            .then(res => {
                this.tags = res.data;
            })
        }
    }
}
</script>
<style scoped>

</style>
