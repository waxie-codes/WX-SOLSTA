<script rel='text/javascript'>
  const h2s = document.querySelectorAll('h2:nth-of-type(even)');
  const nodeArray = ['P', 'H3']

  for (let h2 of h2s) {

    h2.classList.add('greyed');
    var elem = h2.nextElementSibling;

    while (nodeArray.indexOf(elem.nodeName) != "-1") {
      elem.classList.add('greyed');
      elem = elem.nextElementSibling;
    };

  }
</script>
