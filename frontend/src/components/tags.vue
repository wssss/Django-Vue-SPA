<template>
    <div class="widget twitter">
        <h3 class="title">Tags</h3>
        <ul class="entry">
            <li v-for="tag in tags" :key="tag.id">
                <router-link :to="{ name: 'posts', query: { 'tag': tag.id }}">
                    {{tag.name}}
                </router-link>
                <small>{{tag.post_count}}</small>
            </li>
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
                this.tags = res.data.results;
            })
        }
    }
}
</script>
<style scoped>

</style>
