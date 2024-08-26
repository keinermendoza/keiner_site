import './multi_select_tag/styles.css';
import MultiSelectTag from  './multi_select_tag/main';


document.addEventListener("DOMContentLoaded", () => {

    const helper_text = document.getElementById('filter_source_help_text').innerHTML;
    new MultiSelectTag('topics_filter_id', {
        rounded: true,    // default true
        shadow: true,      // default false
        placeholder: 'Search',  // default Search...
        helperText: helper_text,
        tagColor: {
            textColor: '#327b2c',
            borderColor: '#92e681',
            bgColor: '#eaffe6',
        },
        onChange: function(values) {
            const execFilter = new Event("excecute_blog_post_filtering");
            document.body.dispatchEvent(execFilter);
        }
    });
    
})